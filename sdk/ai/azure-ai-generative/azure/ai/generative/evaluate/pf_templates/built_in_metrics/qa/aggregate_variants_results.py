from typing import List
from promptflow import tool, log_metric
import numpy as np
from utils import filter_metrics

@tool
def aggregate_results(results: List[dict], selected_metrics: List[dict], thresholds: List[int]) -> dict:
    selected_safety_metrics = filter_metrics(selected_metrics[0]["safety_metrics"])
    selected_quality_metrics = filter_metrics(selected_metrics[0]["quality_metrics"])

    if thresholds != [] and thresholds is not None:
        threshold = np.float16(thresholds[0])
    else:
        threshold = RAIService.HARM_SEVERITY_THRESHOLD
    print(threshold)

    aggregate_results = {}
    for result in results:
        if not result:
            continue
        for name in result.keys():
            if name in selected_quality_metrics or name in selected_safety_metrics:
                if name not in aggregate_results.keys():
                    aggregate_results[name] = []
                metric_value = result[name]
                if name in selected_safety_metrics:
                    metric_value = result[name + "_score"]
                try:
                    float_val = float(metric_value)
                except Exception:
                    float_val = np.nan
                aggregate_results[name].append(float_val)

    aggregate_output = {}
    for name, value in aggregate_results.items():
        metric_name = name
        if name in selected_quality_metrics:
            aggregate_output[metric_name] = np.nanmean(value)
        elif name in selected_safety_metrics:
            values = aggregate_results[name]
            metric_name = name+'_defect_rate'
            aggregate_output[metric_name] = np.sum(values >= threshold) / len(values)

        aggregate_output[metric_name] = round(aggregate_output[metric_name], 2)
        log_metric(metric_name, aggregate_output[metric_name])
    return aggregate_output

