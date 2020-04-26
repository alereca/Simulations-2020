def general_generate_subplot(figure):
    def specific_generate(metrics_arrays, expected_values, params):
        ax = figure.add_subplot(2, 2, params.position)
        for metrics_array in metrics_arrays:
            ax.plot(metrics_array)
        for expected_value in expected_values:
            ax.axhline(expected_value, color="purple", linestyle="dashed")
        ax.set_title(label=params.title)
        ax.set_xlabel(xlabel=params.xlabel)
        ax.set_ylabel(ylabel=params.ylabel)

    return specific_generate
