def main() -> None:
    player1: str = input("Soccer player ")
    player2: int = input("Jersey number ")
    players: dict[str,int] = zip(player1, player2)
    print(players)
    
def zip(a: list[str], b: list[int]) -> dict[str,int]:
    result: dict[str,int] = {}
    if len(a) != len(b):
        return result
    if len(a) and len(b) == 0:
        return result
    for i in range(len(a)):
        result [a[i]] = b[i]
    return result

if __name__ == "__main__":
    main()