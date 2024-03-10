# Using `print` to debug code.

Open/run the file `using_print.py`. The script is designed to calculate the sum of numbers in a list and then calculate the average. However, there's a bug in the code that causes it to produce an incorrect result.

1. **Identify the Symptom**: 
   - Run the script and observe the output. Suppose it says, "The average is: 0.0," which indicates there's a bug because the average of these numbers should not be 0.0.

2. **Print Input Data**:
   - Add a print statement to confirm that the input data (the list of numbers) is correct.
   ```python
   print(f"Numbers: {numbers}")
   ```

3. **Debug the Sum Function**:
   - Add a print statement inside the `calculate_sum` function to check if the total sum is being calculated correctly.
   ```python
   def calculate_sum(numbers):
       total = 0
       for number in numbers:
           total += number
           print(f"Adding {number}, Total so far: {total}")
       return total
   ```

4. **Debug the Average Function**:
   - Add a print statement to check the result of the sum and the length of the numbers list before calculating the average.
   ```python
   def calculate_average(numbers):
       sum_of_numbers = calculate_sum(numbers)
       print(f"Sum of numbers: {sum_of_numbers}, Count: {len(numbers)}")
       average = sum_of_numbers // len(numbers)
       return average
   ```

5. **Run the Script and Observe**:
   - Run the script again, and observe the printed output to track down where the calculation goes wrong.

6. **Identify and Fix the Bug**:
   - Based on the print statements, you might notice that everything appears correct until the average calculation. If the output is still incorrect, you suspect the bug might be with the division operation.
   - Upon closer inspection, you realize the operator we are using to carry out the division is the operator `//` and not the usual `/`.

7. **Clean Up**:
   - After fixing the bug, remove all the print statements used for debugging to clean up the code.
