import json

stockjsonstring='{"code":0,"msg":"ok","data":{"summary":{"date":"20170901","time":"145959","data":{"cje100":"10, 92, 167512, 18367.74, 110985, 51342, 5185"}},"detail":[["14:59:56","11.17","4601","S"],["14:59:20","11.19","1124","S"],["14:54:46","11.20","6905","B"],["14:52:49","11.13","3907","S"],["14:52:10","11.18","3020","B"],["14:51:52","11.18","933","B"],["14:51:46","11.17","1405","B"],["14:48:06","11.14","969","B"],["14:41:53","11.18","1105","B"],["14:37:49","11.19","1501","S"],["14:36:22","11.21","3201","S"],["14:34:49","11.26","1018","S"],["14:34:22","11.30","3924","B"],["14:33:40","11.29","1073","B"],["14:32:45","11.25","1246","B"],["14:32:42","11.25","1150","B"],["14:32:03","11.23","2172","B"],["14:31:54","11.21","2043","B"],["14:31:48","11.19","2278","S"],["14:31:48","11.20","3137","B"],["14:31:27","11.19","974","B"],["14:30:09","11.15","2101","B"],["14:30:06","11.15","3424","B"],["14:25:23","11.13","1369","B"],["14:11:38","11.08","1332","S"],["14:10:29","11.09","938","B"],["14:08:44","11.04","1118","B"],["14:07:26","11.07","911","S"],["14:06:16","11.11","1355","B"],["13:59:03","11.19","1058","B"],["13:59:00","11.18","1254","S"],["13:58:33","11.17","913","S"],["13:56:33","11.15","1568","S"],["13:55:33","11.20","1592","S"],["13:55:30","11.21","1084","S"],["13:55:21","11.23","908","B"],["13:54:18","11.20","2139","B"],["13:53:51","11.18","1054","B"],["13:53:23","11.12","1004","B"],["13:53:14","11.10","4684","B"],["13:52:38","11.04","1091","S"],["13:52:11","11.03","1682","B"],["13:51:53","11.02","1039","B"],["13:50:02","11.00","1343","B"],["13:45:07","11.00","1015","S"],["13:43:25","11.01","921","B"],["13:42:55","11.07","1139","B"],["13:42:43","11.05","2202","M"],["13:42:40","11.04","1045","S"],["13:42:30","11.05","1010","B"],["13:42:13","11.00","8067","B"],["13:42:03","10.98","2024","B"],["13:41:54","10.95","2628","B"],["13:41:51","10.94","2983","M"],["13:41:27","10.90","2992","B"],["13:41:24","10.90","2844","B"],["13:41:12","10.84","1097","S"],["13:41:06","10.85","1048","B"],["13:41:06","10.85","1124","B"],["13:39:03","10.80","1003","S"],["13:38:12","10.80","3000","B"],["13:33:50","10.81","1389","B"],["13:33:20","10.83","1005","B"],["13:32:50","10.80","2464","B"],["13:32:32","10.80","1630","B"],["13:32:20","10.75","2510","B"],["13:31:41","10.71","3752","B"],["13:31:38","10.70","3705","B"],["13:30:52","10.67","1177","B"],["13:23:15","10.62","2670","B"],["13:23:00","10.62","3317","B"],["13:22:09","10.60","1571","B"],["13:11:49","10.52","1029","S"],["13:10:31","10.52","2011","S"],["13:00:20","10.55","976","S"],["11:28:38","10.55","1206","S"],["10:54:02","10.60","1033","B"],["10:33:53","10.54","1100","B"],["10:32:56","10.53","1004","S"],["10:24:45","10.55","1552","S"],["10:24:45","10.54","1080","S"],["10:24:36","10.55","1026","S"],["10:23:48","10.56","1307","S"],["10:15:23","10.57","1000","S"],["10:03:26","10.56","1055","S"],["10:03:08","10.55","1016","S"],["10:01:08","10.58","1215","S"],["9:43:11","10.69","1593","B"],["9:37:49","10.70","1007","S"],["9:36:25","10.68","1200","S"],["9:31:42","10.58","1129","S"],["9:30:42","10.62","994","S"]]}}'

stockjsonobj=json.loads(stockjsonstring)

print stockjsonobj
