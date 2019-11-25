#
# Store functions
#

# GAME RULES
# Each node has address of its self, 
# and all the other nodes

# GET
# Assuming every node has the most updated dict
# In the future, could ping and await all other nodes for a consistent value
#   In that case,
# 	- current node will have to wait for N nodes to respond,
# 	- with a wait time to kill request if no responses.
# 	- Altogether, a runtime of N * Wait-Time
# 	Design for the future
# 	- Send forwards as a get request to all other nodes
# 	- Collect all responses (even dead ones) in a masterlist,
# 	- Compare and return either:
# 		- the most commonly seen value
# 		- the last seen value (at this point all puts and deletes should have been attached with a timestamp)
#
# For now, get the current node's dictionary value and hold that as truth

# PUT/POST
# Put in current node's dictionary as usual
# Send an update to all other nodes in list, do not await response,
# With a Forwarding boolean parameter, forward if Forward = True else just update
# Otherwise, you'll run into an infinite loop
# 	Design for the future
# 	- Send forwards as a put request to all other nodes
# 	- Are we making timestamp comparisons here? Or just blindly updating
# 	- What about this:
# 		NodeKeyValueStore {
# 			Key: ValueArray[firstValue, secondValue, ...latestValue]
# 		}
# 	- Keep an array of values
# 	- Whenever a node receives a forwarded update,
# 	- Do a comparison for that key in its dictionary
# 	- Append to Key's key value array in order seen

# DELETE
# Delete in current node's dictionary as usual
# Forwarding works the same as a put
# 