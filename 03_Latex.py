import streamlit as st

# title
st.title("Streamlit Latex")

# Matrix
st.markdown("## Matrix of order 2x2:")
# matrix with square brackets
st.latex(r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
# matrix with parentheses
st.latex(r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")
# matrix with vertical bars
st.latex(r"\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix}")
# matrix with curly braces
st.latex(r"\begin{Bmatrix} 1 & 2 \\ 3 & 4 \end{Bmatrix}")


# Equations
st.latex(r"e^{i\pi} + 1 = 0")

st.latex(r"2x^2 + 3x + 1 = 0")

st.latex(r"""\begin{alignat}{2}
   10&x+&3&y=2\\
   3&x+&13&y=4
\end{alignat}""")

st.markdown("[Link for more Latex syntax](https://katex.org/docs/supported.html)")