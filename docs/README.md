# SNMPwalk_to_SNMPrec
Scripts to convert MIB table output to SNMPrec format to mimic networking devices

## Instructions
This is a very simple script to run, but before running, you will need to select a MIB table name from [Online MIB Browser](https://bestmonitoringtools.com/mibdb/mibdb_search.php)
* Example:
![Juniper SNMP MIB browser (OID list) 2022-10-30 at 9 51 51 PM](https://user-images.githubusercontent.com/49233513/198916363-712a045d-ae8c-4ed2-896c-a822640a5583.jpg)



Then you can run the `run.sh` script using the `MIB table name` as a parameter. The `run.sh` script will download the MIB table in `YAML` format and then call the Python script to parse through the data, format it to `snmprec` format and assign random values to the MIBs.

Example run command:
```
./run.sh JUNIPER-FIREWALL-MIB
```
This will return a nice `snmprec` file to use with [SNMP_sandbox](https://github.com/UTXOnly/SNMP_sandbox)
![README md — SNMPwalk_to_SNMPrec 2022-10-30 at 9 56 36 PM](https://user-images.githubusercontent.com/49233513/198916381-4213b37b-1f1d-4166-a062-8fafccbb202a.jpg)