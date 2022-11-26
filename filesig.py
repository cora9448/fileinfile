signatures = [
    "ff d8 ff e0",
    "ff d8 ff e8",
    "47 49 46 38 37 61",
    "47 49 46 38 39 61",
    "89 50 4e 47 0d 0a 1a 0a",
    "25 50 44 46 2d 31 2e",
    "50 4b 03 04",
    "41 4c 5a 01",
    "52 61 72 21 1a 07",
    "50 4b 03 04 14 00 06 00",
    "49 44 33"
]

signatures = list(map(bytes.fromhex, signatures))


def searchFileInFile(filename):
    with open(filename, "rb") as file:
        data = file.read()

        for signature in signatures:
            if signature in data:
                if signature in data[:15] and data.count(signature) == 1:
                    print(
                        f"파일 내부에 {signature.hex()} 파일이 {data.count(signature) - 1} 개 존재합니다.")
            else:
                print(
                    f"파일 내부에 {signature.hex()} 파일이 {data.count(signature)} 개 존재합니다.")


filename = input("File name: ")
searchFileInFile(filename)
