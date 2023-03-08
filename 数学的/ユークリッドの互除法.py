#ユークリッドの互除法

# やり方
# 【step1】: aをbで割り，あまりrを求める
# 【step2】: a, bをb, rでそれぞれ置き換える
# 【step3】: あまりrが0なら，その時の割る数bが最大公約数で，そうでなければstep1へ戻る


def gcd(a, b):
    r = a % b
    #あまりが0でなければ続ける
    while r != 0:
        a, b = b    , r
        r = a % b

    return b

num1 = 100
num2 = 25
# Greatest Common Diviso 最大公約数
GCD = gcd(num1, num2)

print(GCD)
