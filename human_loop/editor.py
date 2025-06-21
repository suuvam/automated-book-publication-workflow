def human_edit(text):
    print("Human-in-loop editor module loaded - Real CLI Editor in use.\n")
    print("--------- Original Content ---------")
    print(text)
    print("-----------------------------------")
    
    choice = input("\nDo you want to edit this content manually? (yes/no): ").strip().lower()

    if choice == "yes":
        print("\nEnter your edited content below. When finished, type 'END' on a new line:")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        edited_text = "\n".join(lines)
        print("\nYour final edited content:")
        print(edited_text)
        return edited_text
    else:
        print("\nKeeping AI-reviewed content without changes.")
        return text
