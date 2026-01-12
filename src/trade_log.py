import pandas as pd


def generate_trade_log(df):
    trades = []

    position = 0
    entry_date = None
    entry_price = None

    for i in range(len(df) - 1):
        current_pos = df["Position"].iloc[i]

        if pd.isna(current_pos):
            current_pos = 0
        else:
            current_pos = int(current_pos)

        next_row = df.iloc[i + 1]

        # Entry
        if position == 0 and current_pos == 1:
            position = 1
            entry_date = next_row.name
            entry_price = float(next_row["Open"].iloc[0])

        # Exit
        elif position == 1 and current_pos == 0:
            exit_date = next_row.name
            exit_price = float(next_row["Open"].iloc[0])

            trade_return = (exit_price / entry_price) - 1
            holding_days = (exit_date - entry_date).days

            trades.append({
                "entry_date": entry_date,
                "exit_date": exit_date,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "return": trade_return,
                "holding_days": holding_days
            })

            position = 0

    return pd.DataFrame(trades)
