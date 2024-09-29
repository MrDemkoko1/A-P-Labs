#               ∞
# Function: x + ∑ 1*3*5...(2n-1) / 2*4*6...(2n)*(2n+1)
#              n=1

start_x = 0.5                                   # Start value for x
end_x = 0.9                                     # End value for x
step = 0.05                                     # Step of x's change
prec = 0.001                                    # Precision to which we tabulate the function

def count_sum():                                # Creating a func that gonna count sum in given prec
    addend = 1                                  # Initialising addend var, 1 value is just for init
    total_sum = 0                               # Initialising total sum var to store fin result in given prec
    n = 1                                       # Start with the 1st term

    while addend >= prec:                       # Loop until the addend is less than prec
        numerator = 1                           # Initialising numerator var
        for i in range(1, n + 1):               # Calculate (1 * 3 * 5 * ... * (2n - 1))
            numerator *= 2 * i - 1              # Multiply the current odd term

        denominator = 1                         # Initialising denominator var
        for i in range(1, n + 1):               # Calculate (2 * 4 * 6 * ... * (2n))
            denominator *= 2 * i                # Multiply the current even term
        denominator *= 2 * n + 1                # Multiply by (2n + 1) for the complete denominator

        addend = numerator / denominator        # Calculate n-st addend
        total_sum += addend                     # Add current addend to the total sum in given prec
        n += 1                                  # Increase n to do the next step of the cycle

    return total_sum                            # Return the total sum in given precision

def tabulate_function():                        # Create a func to tabulate the function
    x = start_x                                 # Initialise x var with starting value

    while x <= end_x:                           # Create a loop to calculate results of func with given step in gien range
        result = x + count_sum()                # Calculate func for given x
        print(f"f({x:.2f}) = {result:.3f}")     # Print result
        x = round(x + step, 2)                  # Update x, rounding to two decimal places (to avoid problems with float precision)

tabulate_function()                             # Call the func to tabulate func (🫠)