N = int(input("ВВедите N:"))
i = N
i -= 1
#начало положено
countAllMax = 0
for k in range(0, i + 1):
    count = 0
    fi = 1
    for i_n in range(2, i + 1):
        fi *= i_n
    fk = 1
    for j in range(2, k + 1):
        fk *= j
    fik = 1
    for i_k in range(2, i - k + 1):
        fik *= i_k

    Cik = fi // (fk * fik)
    while Cik != 0:
        Cik //= 10
        count += 1
    countAllMax += count
countAllMax += N - 1
print("--------------------------")
for i in range(N):
    # рисуем пробелы
    countAllCur = 0
    for k in range(0, i + 1):
        count = 0
        fi = 1
        for i_n in range(2, i + 1):
            fi *= i_n
        fk = 1
        for j in range(2, k + 1):
            fk *= j
        fik = 1
        for i_k in range(2, i - k + 1):
            fik *= i_k
        Cik = fi // (fk * fik)
        while Cik != 0:
            Cik //= 10
            count += 1
        countAllCur += count
    countAllCur += i
    for _ in range((countAllMax - countAllCur) // 2):
        print(" ", end='')

    # вывод коэффициентов
    for k in range(0, i + 1):
        count = 0
        fi = 1
        for i_n in range(2, i + 1):
            fi *= i_n
        fk = 1
        for j in range(2, k + 1):
            fk *= j
        fik = 1
        for i_k in range(2, i - k + 1):
            fik *= i_k
        Cik = fi // (fk * fik)
        print(Cik, end=' ')
    print()
