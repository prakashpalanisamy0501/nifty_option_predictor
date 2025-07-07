def filter_profitable_options(option_chain, direction, spot_price):
    option_type = "CE" if direction == 1 else "PE"
    strike_range = [0, 50, 100]

    suggestions = []

    for data in option_chain:
        for gap in strike_range:
            strike = round(spot_price / 50) * 50 + (gap if direction == 1 else -gap)
            option = data.get(option_type)
            if option and option['strikePrice'] == strike:
                ltp = option['lastPrice']
                iv = option.get('impliedVolatility', 'N/A')
                delta = option.get('delta', 'N/A')
                theta = option.get('theta', 'N/A')

                if ltp and ltp >= 5:
                    suggestions.append({
                        "strike": strike,
                        "type": option_type,
                        "ltp": ltp,
                        "target": round(ltp + 10, 2),
                        "iv": iv,
                        "delta": delta,
                        "theta": theta
                    })
    return suggestions
