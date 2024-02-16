while True:
    try:
        num = int(float(input("Enter a number: ")))
        print(num)
        break
    except ValueError:
        print("That is not a number")
    except KeyboardInterrupt:
        print("\nNo input taken")
        break
    finally:
        print("Attempted input")