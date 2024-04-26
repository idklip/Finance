# def
import os
import sys


def double(a):
    b = "%.2f" % round(a, 2)
    return float(b)


# Increase, Decrease, Payment per period, monthly interest, type of interest, investment
while True:

    qq = 0
    q = -2
    while q < 0:
        qq = str(input("\nAre you looking to calculate Present Value, Interest Rate, "
                       "Annuity/Regular Payments, or Future Value? "
                       "(pv/ir/a/fv): "))

        print("\nEnter [0] if you will not be using a value.")
        if qq == "fv" or qq == "FV":
            P = float(input("\nPresent Value: "))
            r = float(input("\nAPR/Annual Interest [%]: ")) / 100
            A = float(input("\nAnnuity/Regular Payment: "))

            q = 365

        elif qq == "ir" or qq == "IR":
            P = float(input("\nPresent Value: "))
            F = float(input("\nFuture Value: "))
            q = 12

        elif qq == "pv" or qq == "PV":
            r = float(input("\nAPR/Annual Interest [%]: ")) / 100
            A = float(input("\nAnnuity/Regular Payment: "))
            F = float(input("\nFuture Value: "))
            q = 1

        elif qq == "a" or qq == "A":
            P = float(input("\nPresent Value: "))
            F = float(input("\nFuture Value: "))
            r = float(input("\nAPR/Annual Interest [%]: ")) / 100
            q = 12

        else:
            print("Please try again and input what you'd like to calculate.")
            c = -1
            continue


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

    n = 0
    ques = input("\nDo the number of Payment Periods per year differ from the number of Compounding Periods? (y/n): ")

    if ques == "y" or ques == "Y":
        print("Well Shit")

    else:
        n = c

    t = float(input("\nNumber of Years to Calculate: "))

    rc = r / c
    ct = c*t
    nt = n*t

    if qq == "fv" or qq == "FV":
        if P != 0:
            F = P * ((1 + rc) ** nt)
        else:
            F = A * ((((1 + rc)**nt)-1)/rc)

    elif qq == "ir" or qq == "IR":
        rt = (F/P) ** (1/ct)
        r = c * (rt-1)

    elif qq == "pv" or qq == "PV":
        if F != 0:
            P = F / ((1 + rc) ** nt)
        else:
            P = A * ((1 - ((1 + rc) ** (-1 * nt))) / rc)

    elif qq == "a" or qq == "A":
        if P == 0:
            A = (F * rc) / (((1 + rc)**nt)-1)
        else:
            A = (P * rc) / (1 - ((1 + rc) ** (-1 * nt)))

    r = double(r*100)
    t = double(t)
    P = double(P)
    F = double(F)
    tA = double(A*nt)
    A = double(A)
    if F != 0:
        I = double(F - tA - P)
    else:
        I = double(tA - P)

    output = str(f"\n${P:.2f} (Present Value) + ${A:.2f} (Regular Payment) {n} time(s) per year for {t} years "
                 f"(${tA:.2f} Total in Payments) at {r}% (${I:.2f} in Interest) = ${F:.2f} (Final Value)")

    print(output)

    sav = input("\nWould you like to save the output to a file? (y/n): ")
    if sav == "y" or sav == "Y":
        name = input("\nFilename?: ")
        name += ".txt"
        with open(name, 'a') as file:
            file.write(output + "\n")
        print(f"\nInfo has been saved to {name}")

    elif sav == "n":
        print("\nInfo not saved")

    else:
        print("error")

    res = input("\nWould you like to run the command again? (y/n): ")
    if res == "y" or res == "Y":
        continue
    else:
        sys.exit()
