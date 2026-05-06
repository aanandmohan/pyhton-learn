ch=input("enter vowel or cons ").lower()
match ch:
    case"a"|"e"|"i"|"o"|"u":
        print("vowel")
    case "!"|"@"|"#"|"%"|"$"|"&":
        print("special charector")
    case _:
        print("consonent")