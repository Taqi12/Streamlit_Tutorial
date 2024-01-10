# import library
import streamlit as st

# title
st.title("Streamlit Text")

# Text
st.text("Hello, World!")

# Write
st.write("Hello, World!")

# Markdown
st.markdown("# Heading1")
st.markdown("## Heading2")
st.markdown("### Heading3")
st.markdown("#### Heading4")
st.markdown("##### Heading5")
st.markdown("###### Heading6")

# Markdown - Bold
st.markdown("**Bold**")

# Maekdown - Bold and Italic
st.markdown("___Bold and Italic___")

# Markdown - Italic
st.markdown('*italicized text*')

# Markdown - Deleted
st.markdown("~~deleted text~~")

# Markdown - Code
st.markdown("```python\nprint('Hello, World!')\n```")

# Markdown - Blockquote
st.markdown("> blockquote")
st.markdown(">")
st.markdown(">>>>")
st.markdown(">> blockquote")
st.markdown(">>> blockquote")
st.markdown(">> blockquote")
st.markdown(">>>>>>>>>>> blockquote")
st.markdown("""> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.""")

st.markdown("""> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.""")


 # Markdown - Ordered List
st.markdown("1. First item\n2. Second item\n3. Third item")
 # Markdown - Unordered List
st.markdown("- First item\n- Second item\n- Third item")


# Markdown - Line
st.markdown("---")

# Markdown - Links
st.markdown("[Google](https://www.google.com/)")
# Markdown - Image link
st.markdown("![image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)")
# Markdown - Email link
st.markdown("taqijaved7@gmail.com")
# Markdown - Reference link
st.markdown("""Open the goole through the [reference link][1]

[1]: <https://www.google.com/> 
""")

# # Markdown - Table
st.markdown("| Syntax | Description |\n | ----------- | ----------- |\n| Header | Title |\n| Paragraph | Text |")

# Markdown - Fencced Code Blocks
st.markdown("""```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```""")

# Markdown - Footnote
st.markdown("""Here's a sentence with a footnote. [^1] \n [^1]: This is the footnote.""")

# Markdown - jason
st.markdown("""```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```""")

# Markdown - Strikethrough
st.markdown("~~The world is flat.~~")

# Markdown - Task List
st.markdown("- [ ] Write the press release\n- [X] Update the website\n- [ ] Contact the media")


# Markdown - Emoji
st.markdown("That is so funny! :joy:")

st.markdown("That is so funny! :joy: :joy: :joy:")

st.markdown("Heart_eyes :heart_eyes:")

st.markdown("Snowflake :snowflake:")

st.markdown("[Markdown Emoji List](https://gist.github.com/rxaviers/7360908)")