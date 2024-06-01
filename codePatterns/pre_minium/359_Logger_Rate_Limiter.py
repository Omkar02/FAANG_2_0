""" 
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 1, June 2024
"""
# * ---------------------------------------------------------------------------------------------------------------------------------------------
"""
* Example 1:
    Input
        ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
        [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
    Output
        [null, true, true, false, false, false, true]

    Explanation
        Logger logger = new Logger();
        logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
        logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
        logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
        logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
        logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
        logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
"""


class Logger:
    def __init__(self) -> None:
        self.log_history = {}  # * {log_msg: last_seen_time}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.log_history:
            self.log_history[message] = timestamp
            return True
        else:
            last_seen = self.log_history.get(timestamp)
            if timestamp - last_seen >= 10:
                # To check if the time-difference between
                # now and prevous occurange is greater than eq to 10
                self.log_history[message] = timestamp
                return True
            return False
