### redis command to check ceche

```bash
redis-cli -n 1 KEYS ":1:verify:*"
```
directly check redis cache, shows only user emiles that need to be verified their email address. <br />
### command for control redis interaction
```bash
redis-cli monitor  # Shows all GET / POST 
```