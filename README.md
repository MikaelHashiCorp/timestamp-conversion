# timestamp-conversion
Convert Epoch timestamps in Nomad debug bundles to ISO 8601 (YYYY-MM-DDTHH:mm:ss.SSSSSSZ)

* timestamp1.json goes with replace6tm.py - Proof of concept (POC).
* event1.json goes with replace_event1.py - Attempt to apply POC to a snippet of a Nomad operator debug bundle log `eventstream.json`.

* replace6tm.py works
* replace_event1.py doesn't work

* Sites where JSON scan/walk algorythms are:
  * https://stackoverflow.com/questions/66730815/python-replace-nested-dict-keys-value-in-entire-json-whether-inside-a-list-or
  * https://stackoverflow.com/questions/55704719/python-replace-values-in-nested-dictionary
