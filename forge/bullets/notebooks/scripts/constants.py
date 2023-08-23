"""
This is the regex for a standard bullet pattern "-[ACTION];[IMPACT]--[OUTCOME]"
The pattern is not all-encompassing - this hardcoded value can to be experimented with
to achieve maximum bullet capture
"""
bullet_pattern = r"^-?([\w\W\s]{0,255});?([\w\W\s]{0,255})--([\w\W\s]{0,255})$"

"""
Input prefix used for fine tuning the model to comprehend as a key word for
bullet creation tasking
"""
bullet_prompt_prefix = "Create a Air and Space Force bullet statement from the following: "

"""
Input prefix used for fine tuning the model to comprehend as a key word for
bullet creation tasking
"""
bullet_data_creation_prefix = "Expand upon the following Air and Space Force bullet by removing acronyms, adding filler context, and using at least 3 full sentences: "