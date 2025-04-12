def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Reverse the list
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Append "orange" to the end
    fruit_list.append("orange")
    print(f"after appending orange: {fruit_list}")

    # Insert "cherry" before "apple"
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(f"after inserting cherry before apple: {fruit_list}")

    # Remove "banana"
    fruit_list.remove("banana")
    print(f"after removing banana: {fruit_list}")

    # Pop the last element
    last_item = fruit_list.pop()
    print(f"popped item: {last_item}")
    print(f"after popping: {fruit_list}")

    # Sort the list
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    # Clear the list
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

# Call main to start this program
if __name__ == "__main__":
    main()
