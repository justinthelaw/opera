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
bullet_prompt_prefix = (
    "Using the following Air and Space Force bullet statement format, where special characters are always of the same exact order and type, "
    + "`- [ACTION]; [IMPACT]--[RESULT] `, write an Air and Space Force bullet statement from the following details: "
)

"""
Input prefix used for fine tuning the model to comprehend as a key word for
bullet creation tasking
"""
bullet_data_creation_prefix = "Using full sentences, expand upon the following Air and Space Force bullet statement by spelling-out acronyms and adding additional context: "
