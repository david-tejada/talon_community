question: "?"
(downscore | underscore): "_"
dash: "-"
double dash: "--"
triple quote: "'''"
(triple grave | triple back tick | gravy): insert("```")
(dot dot | dotdot): ".."
ellipsis: "..."
(comma and | spam): ", "
punch: ": "
punch roll:
    edit.line_end()
    ":\n"
sprint:
    key(right)
    ", "
sprint roll:
    edit.line_end()
    ",\n"
plus: "+"
arrow: "->"
dub arrow: "=>"
new liner: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dub string: user.insert_between('"', '"')
empty escaped (dub string | dub quotes): user.insert_between('\\"', '\\"')
empty string: user.insert_between("'", "'")
empty escaped string: user.insert_between("\\'", "\\'")
(inside parens | args): user.insert_between("(", ")")
inside (squares | brackets | square brackets | list): user.insert_between("[", "]")
inside (braces | curly brackets): user.insert_between("{", "}")
inside percent: user.insert_between("%", "%")
inside (quotes | string): user.insert_between("'", "'")
inside (double quotes | dub quotes): user.insert_between('"', '"')
inside (graves | back ticks): user.insert_between("`", "`")
angle that:
    text = edit.selected_text()
    user.paste("<{text}>")
(square | bracket | square bracket) that:
    text = edit.selected_text()
    user.paste("[{text}]")
(brace | curly bracket) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
paren it:
    text = edit.selected_text()
    user.paste("({text})")
percent it:
    text = edit.selected_text()
    user.paste("%{text}%")
quote it:
    text = edit.selected_text()
    user.paste("'{text}'")
(double quote | dub quote) that:
    text = edit.selected_text()
    user.paste('"{text}"')
(grave | back tick) it:
    text = edit.selected_text()
    user.paste("`{text}`")
