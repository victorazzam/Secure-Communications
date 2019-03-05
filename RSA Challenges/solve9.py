# Dan Boneh's book: Twenty Years of Attacks on the RSA Cryptosystem, Hastad’s Broadcast Attack, Page 208
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA
# https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Theorem_statement
# https://pequalsnp-team.github.io/writeups/crypto400_1
# http://www.pwntester.com/blog/2014/01/17/hackyou2014-crypto400-write-up

from gmpy2 import invert
from functools import reduce

Ns = (1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627,405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309,1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723)
Cs = (613757444204638278262310351562876531607487738717774407185252131147104492450160428757483976067628603514761619532764928239807564974590961450735755461481051283186240767490110455431475543041011912015289781128865893349142785039408178696523937605624371679605130950843591197358935516266254687080122972023592091964871,22657108022478695797486965023447848250682406595690518779077232421899889165762724488153241456845951937121308084431913683848889272505486222688188138471999687468256556616878979818168438370975399291696045396880071048188564812795530986969364538462949239012254381251606438993964309325106863727351705595563360310007,311096000497881387953904724284440481805457233048982756757007020410000443330941053703716829538086459727079448020579354693958905904778381820371160626001594619419169121166486655254993091181369105737797409452734836563374374511516011594235202125201067840325349354834604004321427713901643355933701994777952169157646)
e = 3

# Chinese Remainder Theorem
def crt(n, a):
    total = 0
    product = reduce(int.__mul__, n)
    for N, A in zip(n, a):
        tmp = product // N
        total += A * tmp * invert(tmp, N)
    return int(total % product)

# Many attempts and OverflowErrors later, a better solution...
def get_m(C):

    # Find length of m = C ^ (1/e)
    zeros = 1
    while 1:
        if int("1" + "0" * zeros) ** e < C and int("9" * (zeros + 1)) ** e > C:
            break
        zeros += 1
    m = "1" + "0" * zeros

    # Enumerate m = C ^ (1/e)
    for y in range(len(m)):
        M = m[:y], m[y+1:]
        for x in range(1, 10):
            tmp = int(str(x).join(M))
            if tmp ** e < C:
                m = str(x).join(M)
            elif tmp ** e > C:
                m = str(x - 1).join(M)
                break
            else:
                return tmp

# C such that C = m^3 mod n1*n2*n3
C = crt(Ns, Cs)

# Get the plaintext as an integer
m = get_m(C)

# Print the secret message
print(bytes.fromhex(hex(m)[2:]).decode())