import os
import shutil

pr = print
MainDir = "C:\\Users\\admin\\Desktop\\python"

pr("Welcome to the automatic file manager!")

while True:
    pr("Current directory:", os.getcwd())
    action = input("Choose an action. (X = new file, Y = new folder, Q = delete, HELP = other operations, EXIT = exit): ").strip().lower()

    if action == "exit":
        pr("Program terminated. Goodbye!")
        break

    elif action == "x":
        file_name = input("Enter the new file name (full name + extension): ").strip()
        add_content = input("Do you want to add content? Enter 1 for yes, 0 for no: ").strip()

        if add_content == "1":
            content = input("Enter file content: ")
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            pr(f"File '{file_name}' created (with content).")
        else:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("")
            pr(f"File '{file_name}' created.")

    elif action == "y":
        folder_name = input("Enter the new folder name: ").strip()
        create_file = input("Do you want to create a file inside the folder? Enter 1 for yes, 0 for no: ").strip()

        os.mkdir(folder_name)
        pr(f"Folder '{folder_name}' created.")

        if create_file == "1":
            new_dir = os.path.join(MainDir, folder_name)
            os.chdir(new_dir)
            pr("Changed to new directory:", os.getcwd())

            file_name = input("Enter the new file name (full name + extension): ").strip()
            add_content_inside = input("Do you want to add content? Enter 1 for yes, 0 for no: ").strip()

            if add_content_inside == "1":
                content = input("Enter file content: ")
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(content)
                pr(f"File '{file_name}' created (with content).")
            else:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write("")
                pr(f"File '{file_name}' created.")

    elif action == "q":
        target_type = input("Enter 1 to delete a file, 2 to delete a folder: ").strip()

        if target_type == "1":
            file_name = input("Enter the file name (full name + extension) to delete: ").strip()
            os.remove(file_name)
            pr(f"File '{file_name}' deleted.")

        elif target_type == "2":
            folder_name = input("Enter the folder name to delete: ").strip()
            if os.path.isdir(folder_name):
                shutil.rmtree(folder_name)
                pr(f"Folder '{folder_name}' and its contents deleted.")
            else:
                pr("Folder not found or already deleted.")

    elif action == "help":
        help_choice = input(
            "(1) Rename file\n"
            "(2) Show current directory\n"
            "(3) Open file\n"
            "(4) Change to C:\\ root directory\n"
            "(5) Check if file exists\n"
            "(6) Change file extension\n"
            "(7) Get file size\n"
            "(8) Copy and paste (optional rename)\n"
            "(9) Cut and paste\nYour choice: "
        ).strip()

        if help_choice == "1":
            old_name = input("Enter the current file name: ").strip()
            new_name = input("Enter the new file name (full name + extension): ").strip()
            os.rename(old_name, new_name)
            pr(f"File name changed from '{old_name}' to '{new_name}'.")

        elif help_choice == "2":
            pr("Current directory:", os.getcwd())

        elif help_choice == "3":
            target_file = input("Enter the file name to open: ").strip()
            os.startfile(target_file)

        elif help_choice == "4":
            os.chdir("C:\\")
            pr("Changed to C:\\ root directory.")

        elif help_choice == "5":
            check_file = input("Enter the file name to check: ").strip()
            if os.path.exists(check_file):
                pr(f"File '{check_file}' exists.")
            else:
                pr("File not found.")

        elif help_choice == "6":
            file_name = input("Enter the file name to change extension: ").strip()
            new_ext = input("Enter the new extension (example: .txt): ").strip()
            base = os.path.splitext(file_name)[0]
            os.rename(file_name, base + new_ext)
            pr(f"File renamed to: {base + new_ext}")

        elif help_choice == "7":
            file_name = input("Enter the file name to get its size: ").strip()
            size = os.path.getsize(file_name)
            pr(f"File size: {size} bytes ({size / 1024:.2f} KB)")

        elif help_choice == "8":
            source_file = input("Enter the file name to copy: ").strip()
            target_dir = input("Enter the target directory (leave empty for current directory): ").strip()
            if not target_dir:
                target_dir = os.getcwd()
            new_name = input("Enter new name (leave empty to keep the same): ").strip()
            if new_name:
                target_path = os.path.join(target_dir, new_name)
            else:
                target_path = os.path.join(target_dir, os.path.basename(source_file))
            shutil.copy2(source_file, target_path)
            pr(f"File '{source_file}' copied to '{target_path}'.")

        elif help_choice == "9":
            source_file = input("Enter the file name to move: ").strip()
            target_dir = input("Enter the target directory (leave empty for current directory): ").strip()
            if not target_dir:
                target_dir = os.getcwd()
            target_path = os.path.join(target_dir, os.path.basename(source_file))
            shutil.move(source_file, target_path)
            pr(f"File '{source_file}' moved to '{target_path}'.")

        else:
            pr("Invalid choice.")

    else:
        pr("Invalid action. Please try again.")
