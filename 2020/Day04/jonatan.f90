!What am I doing with my life? Coding Fortran? Please send help

!Update passport field containing thingie
SUBROUTINE update_passport(instring, substring, res)
	INTEGER, INTENT(INOUT) :: res
	CHARACTER(200) :: instring
	CHARACTER(3), INTENT(IN) :: substring
	INTEGER :: result
	
	!If exists, set as 1. Else keep as-is
	result = INDEX(instring, substring)
	IF (result > 0) THEN
		res = 1
	END IF
	
END SUBROUTINE update_passport

program jonatan
	implicit none
	
	integer :: ios
	integer, parameter :: read_unit = 99
	character(len=200), allocatable :: lines(:)
	character(len=200) :: line
	integer :: n, i
	integer :: num_valid, num_passports
	character(len=20), dimension(20) :: cols
	integer :: nargs
	integer :: result
	integer :: byr, iyr, eyr, hgt, hcl, ecl, pid, cid
	
	open(unit=read_unit, file='input_jonatan.txt', iostat=ios)
	
	n = 0

	do
		read(read_unit, '(A)', iostat=ios) line
		if (ios /= 0) exit
		n = n + 1
	end do
	
	print*, "File contains ", n, "lines!"
	
	allocate(lines(n)) !Allocate memory
	
	rewind(read_unit) !Like a VHS! Everything is retro
	
	!Read all lines?
	do i = 1, n
		read(read_unit, '(A)') lines(i) !Read this line into lines array at pos i
	end do
	
	!Close the file pointer?
	close(read_unit)
	
	!Process all lines, one by one
	!byr, iyr, eyr, hgt, hcl, ecl, pid, cid
	num_valid = 0
	num_passports = 0
	do i = 1, n
		
		line = lines(i)
		
		!Process the line
		call update_passport(line, "byr", byr)
		call update_passport(line, "iyr", iyr)
		call update_passport(line, "eyr", eyr)
		call update_passport(line, "hgt", hgt)
		call update_passport(line, "hcl", hcl)
		call update_passport(line, "ecl", ecl)
		call update_passport(line, "pid", pid)
		call update_passport(line, "cid", cid)
		
		print*, line
		
		IF (line == "" .OR. i == 1 .OR. i == n) THEN
			
			cid = 1 !Ignore this one for now
			
			IF (byr==1 .AND. iyr==1 .AND. eyr==1 .AND. hgt==1 .AND. hcl==1 .AND. ecl==1 .AND. pid==1 .AND. cid==1) THEN
				num_valid = num_valid + 1
				print*, "Valid!"
			END IF
			
			print*, "NEW PASSPORT GOES HERE!"
			num_passports = num_passports + 1
			byr = 0
			iyr = 0
			eyr = 0
			hgt = 0
			hcl = 0
			ecl = 0
			pid = 0
			cid = 0
		END IF
		
	end do
	
	
	print*, num_valid, " valid passports, out of ", num_passports, " total"

end program
