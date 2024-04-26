import math
# def

def double(a):
    b = "%.2f" % round(a, 2)
    return float(b)

# Increase, Decrease, Payment per period, monthly interest, type of interest, investment

qq = 0
q = -2
while q < 0:
    qq = str(input("\nAre you looking to calculate principal/initial balance, final balance,"
                   " or interest rate? (ib/fb/ir): "))

    if qq == "fb" or qq == "FB":
        P = float(input("\nPrincipal/Initial Balance: "))
        r = float(input("\nAPR/Annual Interest [%]: ")) / 100

        q = 365

    elif qq == "ir" or qq == "IR":
        P = float(input("\nPrincipal/Initial Balance: "))
        A = float(input("\nFinal Balance: "))
        q = 12

    elif qq == "ib" or qq == "IB":
        r = float(input("\nAPR/Annual Interest [%]: ")) / 100
        A = float(input("\nFinal Balance: "))
        q = 1

    else:
        print("Please try again and input whether you'd like to calculate Initial Balance, Final Balance, or Interest Rate.")
        c = -1
        continue

d = float(input("\nAdded Expense/Down Payment (+/-): "))


cc = 0
c = -2
while c < 0:
    cc = str(input("\nHow often does interest compound per year? ([D]aily/[M]onthly/[Y]early/[C]ustom): "))

    if cc == "D" or cc == "d":
        c = 365

    elif cc == "M" or cc == "m":
        c = 12

    elif cc == "Y" or cc == "y":
        c = 1

    elif cc == "C" or cc == "c":
        c = int(input("\nCustom Compound Period (per year): "))

    else:
        print("Please try again and input a correct value.")
        c = -1
        continue

t = float(input("\nNumber of Years to Calculate: "))

if qq == "fb" or qq == "FB":
    mod = (1 + (r / c)) ** (c * t)
    P = P + d
    A = double(P * mod)

elif qq == "ir" or qq == "IR":
    rt = (A/P) ** (1/(c*t))
    r = c * (rt-1)

elif qq == "ib" or qq == "IB":
    mod = (1 + (r / c)) ** (c * t)
    P = double(A / mod)

r = double(r*100)
I = double(A - P)

print(f"\n${P} (Principle) + ${I} ([{r}%] Interest) = ${A} (Total w/o Monthly Payment) \n")

arb = -2
while arb < 0:
    m = input("Would you like to calculate a monthly payment/contribution plan? (y/n): ")
    if m == "n" or "N":
        quit()

    elif m != "n" or "N" or "y" or "Y":
        print("Please enter y or n \n")
        arb = -1

    else:
        arb = 1

mA = P * ((1+(r/c))**c)

#arb2 = -2
#while arb2 < 0:
    #ba = input("Will you start paying before or after interest accumulates? (b/a): ")
    #if ba == "b" or "B":


    #elif ba == "a" or "A":


    #else:
        #print("Please enter b or a \n")
        #arb2 = -1




