import time, random
def encryptor(message, key):
    ld = False
    if(len(message) % 2 != 0):
        message+="z"
        ld = True
    cipher = matrixMult(message, key)
    if(ld):
        cipher = cipher[:len(cipher)-1]
    return cipher

def matrixMult(text, matrix):
    product = ""
    for i in range(0, len(text), 2):
        ft = ord(text[i])-97
        sc = ord(text[i+1])-97
        product+=chr((ft*matrix[0]+sc*matrix[1])%26+97)+chr((ft*matrix[2]+sc*matrix[3])%26+97)
    return product

def decryptor(cipher, key):
    modularInverse = modInverse(key[0]*key[3]-key[1]*key[2], 26)
    key = [key[3]*modularInverse, -key[1]*modularInverse, -key[2]*modularInverse, key[0]*modularInverse]
    return encryptor(cipher, key)


def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def stressTester():
    averageBrute = 0
    averageAttack = 0
    for i in range(10):
        key = []
        message = ""
        for i in range(4):
            key.append(random.randint(1,25))
        for i in range(10):
            message+=chr(random.randint(1,25)+97)
        cipher = encryptor(message, key)
        print(message, cipher, key)
        startTime = time.perf_counter()
        bruteForce(0,[],cipher,message)
        endTime = time.perf_counter()
        averageBrute+=endTime-startTime
        startTime = time.perf_counter()
        if(linearEquationAttack(message, cipher) != message):
            print(linearEquationAttack(message, cipher))
        endTime = time.perf_counter()
        averageAttack+=endTime-startTime
    print("Brute Force Average: " + str(averageBrute))
    print("Attack Time Average: " + str(averageAttack))

def bruteForce(index, key, cipher, message):
    if(index < 4):
        for i in range(0, 26):
            k = key[:]
            k.append(i)
            ft = bruteForce(index+1, k, cipher, message)
            if(ft != False):
                return True
    else:
        if(decryptor(cipher, key) == message):
            return True
    return False

def linearEquationAttack(plaintext, cipher):
    a1 = [ord(plaintext[0])-97,ord(plaintext[1])-97,ord(cipher[0])-97]
    a2 = [ord(plaintext[0])-97,ord(plaintext[1])-97,ord(cipher[1])-97]
    a3 = [ord(plaintext[2])-97,ord(plaintext[3])-97,ord(cipher[2])-97]
    a4 = [ord(plaintext[2])-97,ord(plaintext[3])-97,ord(cipher[3])-97]
    key = linearEquationSolver(a1,a3)
    k1 = linearEquationSolver(a2,a4)
    key.append(k1[0])
    key.append(k1[1])
    return decryptor(cipher, key)

def linearEquationSolver(eq, eq1):
    ogeq = eq[:]
    lcm = compute_lcm(eq[0], eq1[0])
    if(eq[0] != 0):
        eq[1]*=lcm/eq[0]
        eq[2]*=lcm/eq[0]
    if(eq[1] != 0):
        eq1[1]*=lcm/eq1[0]
        eq1[2]*=lcm/eq1[0]
    ft = (eq1[1]-eq[1])%26
    sc = (eq1[2]-eq[2])%26
    val = 0
    for i in range(0, 26):
        if((sc+i*26)%ft == 0):
           val = i
           break
    ret = [((sc+i*26)/ft)%26]

    ft = ogeq[0]
    sc = ogeq[2]-ogeq[1]*ret[0]
    for i in range(0, 26):
        if((sc+i*26)%ft == 0):
           val = i
           break
    ret.append(((sc + i * 26) / ft)%26)
    ret = [int(ret[1]),int(ret[0])]
    return ret
stressTester()

