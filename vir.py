# 1. รับชื่อเครื่องจากผู้ใช้ แล้วลบช่องว่างรอบ ๆ
pc_name = input("Enter PC name: ").strip()

# 2. รับรายชื่อไฟล์ โดยให้กรอกชื่อไฟล์คั่นด้วย comma (,) แล้วลบช่องว่างรอบ ๆ
files_input = input("Enter file names (comma separated): ")

# 3. ถ้าเป็นเครื่อง GUITAR เราถึงจะสแกนไวรัส
if pc_name.upper() == "GUITAR":
    # 4. แปลงสตริงของไฟล์ให้เป็นรายการ
    file_list = [name.strip() for name in files_input.split(",")]

    # 5. เตรียมลิสต์เก็บชื่อไฟล์ที่ “สะอาด” (ไม่มีอักขระพิเศษ)
    clean_files = []

    # 6. ตรวจทีละไฟล์
    for name in file_list:
        valid = True
        # 7. ตรวจทีละตัวอักษร ถ้ามีตัวไหนไม่ใช่ a–z, A–Z, 0–9 ให้ mark ว่าไม่ valid
        for ch in name:
            if not ch.isalnum():
                valid = False
                break
        # 8. ถ้าทุกตัวอักษรผ่าน เราถือว่าเป็นไฟล์ปกติ (ไม่ใช่ไวรัส) ก็เก็บไว้
        if valid:
            clean_files.append(name)

    # 9. แสดงผลเฉพาะรายชื่อไฟล์ที่สะอาด
    #    [Me, WERT] เป็นต้น
    print(f"{pc_name.upper()}:[{', '.join(clean_files)}]")

else:
    # ถ้าไม่ใช่ GUITAR ก็ไม่ทำอะไร
    print("This PC is not GUITAR. No scan performed.")
