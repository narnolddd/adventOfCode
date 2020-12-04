import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object rgc {
    def main(args: Array[String]) = {
        val map= Source.fromFile("rgcinput.txt").getLines().to[Array]
        var passport= Array[String]()
        var count= 0
        var scount= 0
        var kvs= Map[String,String] ()
        for (m <- map) {
            if (m.trim.isEmpty) {
                kvs= parsePassport(passport)
                if (passportRequire(kvs,Array("byr","iyr","eyr","hgt","hcl","ecl","pid"))) {
                    count= count+1
                    if (passportRequireStrict(kvs)) {
                        scount= scount+1
                    }
                }
                passport= Array[String]()
            } else {
                passport=passport:+m
            }
        }
        if (passportRequire(kvs,Array("byr","iyr","eyr","hgt","hcl","ecl","pid"))) {
            count= count+1
            if (passportRequireStrict(kvs)) {
                scount= scount+1
            }
        }
        
        println("Part 1 count",count)
        println("Part 2 count",scount)
    }
    
    // Parse an array of strings to get 
    def parsePassport (passport: Array[String]) : Map[String,String] = {
        var kvs= Map[String,String] ()
        for (p <- passport) {
            //println(p)
            for (kv <- p.split(" ")) {
                //kvs += ("hi" -> "there")
                kvs += ( kv.split(":")(0) ->  kv.split(":")(1)) //  UGH!
            }
        }
        return kvs
    }
    
    def passportRequire(kvs  : Map[String,String] , reqs: Array[String]) : Boolean = {
        
        for (r<-reqs) {
            //println("Check",r)
            if (!(kvs contains r)) {
                return false
            }
        }
        true
    }
    
    def passportRequireStrict(kvs  : Map[String,String]) : Boolean = {
        val byr= kvs("byr").toInt
        if (byr <1920 | byr > 2002) {
            println("Wrong byr",byr)
            return false
        }
        val iyr= kvs("iyr").toInt
        if (iyr <2010 | iyr > 2020) {
            println("Wrong iyr",iyr)
            return false
        }
        val eyr= kvs("eyr").toInt
        if (eyr <2020 | eyr > 2030) {
            println("Wrong eyr",eyr)
            return false
        }
        val hcl= kvs("hcl") 
        if (!(hcl.matches("^#[0-9a-f]{6}$"))) {
            println("Wrong hcl",hcl)
            return false
        }
        val pid= kvs("pid") 
        if (! pid.matches("^[0-9]{9}$")) {
            println("Wrong pid",pid)
            return false
        }
        val ecl= kvs("ecl")
        if (! (Array("amb","blu","brn","gry","grn","hzl","oth").contains(ecl))) {
            println("Wrong ecl",ecl)
            return false
        }
        val hgt = kvs("hgt")
        val hnum= hgt.split("\\D+").head.toInt
        val hstr= hgt.takeRight(2)
        if (! ((hstr == "cm" && Range(150,194).contains(hnum)) | (hstr == "in" && Range(59,77).contains(hnum))) ) {
            println("Wrong hgt",hgt)
            return false
        }
        return true
    }
}
