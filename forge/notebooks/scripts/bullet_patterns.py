# This is the regex for a standard bullet pattern "-<ACTION>;<IMPACT>--<OUTCOME>"
# The pattern is not all-encompassing - this hardcoded value can to be experimented with
# to achieve maximum bullet capture
BULLET_PATTERN = r"^-?([\w\W\s]{0,255});?([\w\W\s]{0,255})--([\w\W\s]{0,255})$"

BULLET_PROMPT_PREFIX = "Summarize in format: -[ACTION];[IMPACT]--[OUTCOME]: "
