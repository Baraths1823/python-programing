import numpy as np
print("First Wednesday in 2022:")
print(np.busday_offset('2022', 0, roll='forward', weekmask='Wed'))
