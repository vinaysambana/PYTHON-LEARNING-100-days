
# Section 1: Basic String Manipulation

# 1. Student Name Formatter
name = "sAkEtH kAlLePu"
print("1. Student Name Formatter:")
print(name.title())  # Saketh Kallepu
print()

# 2. Customer Email Cleanup
email = " Saketh.KALLEPU@GMAIL.COM "
print("2. Customer Email Cleanup:")
print(email.strip().lower())  # saketh.kallepu@gmail.com
print()

# 3. Product Code Replacement
product_code = "OLD-101-OLD-202"
print("3. Product Code Replacement:")
print(product_code.replace("OLD", "NEW"))  # NEW-101-NEW-202
print()

# 4. Username Generator
first_name = "SAKETH"
year = 2027
username = first_name.lower() + "_" + str(year)
print("4. Username Generator:")
print(username)  # saketh_2027
print()

# 5. Sentence Character Count (including spaces)
sentence = "Python makes coding easy"
print("5. Sentence Character Count:")
print(len(sentence))  # 24
print()

# Section 2: Indexing and Slicing

# 6. Employee ID Extraction
employee_id = "EMP582741"
print("6. Employee ID Extraction:")
print(employee_id[3:])  # 582741
print()

# 7. Mask a Bank Account Number
account_number = "123456789012"
masked_account = "*" * 8 + account_number[-4:]
print("7. Mask a Bank Account Number:")
print(masked_account)  # ********9012
print()

# 8. Alternating Character Extraction
text = "CODEGNANPYTHON"
print("8. Alternating Character Extraction:")
print(text[::2])  # CDGAPTO
print()

# 9. Reverse a Product Serial Number
serial_number = "PYTHON123"
print("9. Reverse a Product Serial Number:")
print(serial_number[::-1])  # 321NOHTYP
print()

# 10. Extract a File Extension (last three characters)
filename = "student_report.pdf"
print("10. Extract a File Extension:")
print(filename[-3:])  # pdf
print()

# Section 3: Searching, Splitting, and Joining

# 11. Search for a Course Name (case-insensitive substring count)
description = "Python is easy. I love PYTHON. Learn python today."
print("11. Search for a Course Name:")
print(description.lower().count("python"))  # 3
print()

# 12. Convert a Sentence into Words
sentence = "Learn Python Full Stack Development"
print("12. Convert a Sentence into Words:")
print(sentence.split())
# ['Learn', 'Python', 'Full', 'Stack', 'Development']
print()

# 13. Generate a Formatted Address
house = "12-4"
street = "MG Road"
city = "Vijayawada"
state = "Andhra Pradesh"
address = ", ".join([house, street, city, state])
print("13. Generate a Formatted Address:")
print(address)  # 12-4, MG Road, Vijayawada, Andhra Pradesh
print()

# 14. Count Words in a Message (without using loops)
message = "Your application has been successfully submitted"
print("14. Count Words in a Message:")
print(len(message.split()))  # 6
print()

# 15. Validate a Coupon Code
coupon_code = "CODEGNAN"
print("15. Validate a Coupon Code:")
print(coupon_code.isalpha())  # True

# Additional Question
coupon_code = "CODEGNAN123"
print(coupon_code.isalpha())  # False
