from colorama import Fore, Back, Style, init

init(autoreset=True)

# 2. Bright bold heading
def heading_bold(text):
    print(Fore.GREEN + Style.BRIGHT + text)

# 3. Underlined heading
def heading_underlined(text):
    print(Fore.YELLOW + text)
    print(Fore.YELLOW + '-' * len(text))

# 4. Box heading
def heading_box(text):
    print(Fore.MAGENTA + '+' + '-' * (len(text) + 2) + '+')
    print(Fore.MAGENTA + Style.BRIGHT+ f"| {text} |")
    print(Fore.MAGENTA + '+' + '-' * (len(text) + 2) + '+')

# 5. Highlighted background heading
def heading_highlight(text):
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + f"  {text}  ")

# 6. Two-color gradient heading
def heading_gradient(text):
    print(Fore.RED + '=== ' + Fore.YELLOW + text + Fore.RED + ' ===')

# 7. Arrow heading
def heading_arrow(text):
    print(Fore.CYAN + f"-->  {text}  <--")

# 10. Centered heading
def heading_center(text, width=60):
    print(Fore.GREEN + Style.BRIGHT + (" "+text+" ").center(width, '='))


# heading_bold("My Heading")
# heading_underlined("My Heading")
# heading_box("My Heading")
# heading_highlight("My Heading")
# heading_gradient("My Heading")
# heading_arrow("My Heading")
# heading_center("My Heading")
