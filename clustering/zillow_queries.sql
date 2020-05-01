USE zillow;

SELECT prop.*, pred.logerror, 
FROM properties_2017 AS prop
LEFT JOIN predictions_2017 AS pred USING(parcelid)
WHERE YEAR(pred.transactiondate) = 2017;

SELECT MAX(transactiondate) AS max_trans_date
FROM predictions_2017 AS pred
GROUP BY parcelid;

SELECT parcelid, logerror, MAX(transactiondate) AS transaction_date
FROM predictions_2017 AS pred
WHERE YEAR(transactiondate) = 2017
GROUP BY parcelid;

SELECT , pred.logerror,;

SELECT prop.*, pred.logerror, pred.transactiondate
FROM properties_2017 AS prop
LEFT JOIN predictions_2017 AS pred USING(parcelid)
WHERE YEAR(pred.transactiondate) = 2017;

SELECT prop.*, pred.logerror, (SELECT p)
FROM properties_2017 AS prop
LEFT JOIN predictions_2017 AS pred USING(parcelid)
WHERE YEAR(pred.transactiondate) = 2017;

SELECT prop.*
FROM properties_2017 AS prop
LEFT JOIN (SELECT parcelid, MAX(transactiondate) AS max_trans_date
FROM predictions_2017
WHERE YEAR(transactiondate) = 2017
AND WHERE prop.latitude 
GROUP BY parcelid) AS s ON prop.parcelid = s.parcelid;

SELECT prop.*, pred.logerror, pred.transactiondate
FROM properties_2017 AS prop
JOIN predictions_2017 AS pred ON prop.parcelid = pred.parcelid
WHERE prop.latitude IS NOT NULL
AND prop.longitude IS NOT NULL
AND pred.transactiondate IN (
	SELECT MAX(pred.transactiondate)
	FROM predictions_2017 AS pred
	WHERE YEAR(pred.transactiondate) = 2017
	GROUP BY pred.parcelid);





