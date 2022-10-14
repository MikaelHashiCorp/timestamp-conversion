import datetime
import json


## Convert epoch time format to ISO-8601 format.
def convert_time(epoch_nano):
  epoch_micro = epoch_nano / 1000000000.0
  iso8601_micro = datetime.datetime.fromtimestamp(epoch_micro).strftime('%Y-%m-%dT%H:%M:%S.%f000Z')
  return iso8601_micro


## Find the timestamp based by key and modify it.
def update_key_value(var, key):
  if hasattr(var,'items'):
    for k, v in var.items():
      if k == key:
        epoch_nano = int(var[k])
        iso8601_micro = convert_time(epoch_nano)
        var[k] = iso8601_micro
      if isinstance(v, dict):
          update_key_value(v, key)
      elif isinstance(v, list):
        for d in v:
          update_key_value(d, key)


def main():
  ## Read the file.
  with open('event1.json', 'r') as JsonFile:
    data = json.load(JsonFile)

  key = "CreateTime"
  update_key_value(data, key)

  ## Write to the file, replacing the original data.
  with open('event1.json', 'w') as JsonFile:
    # JsonFile.seek(0)  # rewind
    json.dump(data, JsonFile)
    # JsonFile.truncate()  # clean up the bottom

if __name__ == "__main__":
    main()
