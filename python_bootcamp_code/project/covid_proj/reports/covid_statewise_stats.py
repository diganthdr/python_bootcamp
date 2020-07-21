
def get_total_cases(state_name, statewise_data):
    #print("get_total_cases:", state_name, statewise_data)
    count = 0

    for state, dist_data in statewise_data.items():
        if state  not in state_name or not isinstance(dist_data, dict):
            continue
        
        for dist, dist_value in dist_data.items(): 
            if not isinstance(dist_value, dict):
                continue

            for d_name, d_val in dist_value.items():
                if not isinstance(dist_value, dict):
                    continue

                for key, value in d_val.items():
                    if key == "active":
                        count = count + int(value)
    return count


if __name__ == "__main__":
    #get_total_cases("Karnataka", )
    pass