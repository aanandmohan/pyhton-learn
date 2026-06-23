def light(n):
    if n<=1:
        return n
    return light(n-1)+light(n-2)

def main():
    for i in range(7):
        print(light(i),end="")
main()
