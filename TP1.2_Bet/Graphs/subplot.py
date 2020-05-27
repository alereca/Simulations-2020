def general_generate_subplot(figure):
    def specific_generate(metrics_arrays, params):
        ax = figure.add_subplot(2, 2, params.position)
        for metrics_array in metrics_arrays:
            ax.plot(
                metrics_array.data,
            )
            if metrics_array.expected_value:
                ax.axhline(
                    metrics_array.expected_value,
                    linestyle="dashed",
                )
        ax.set_title(label=params.title)
        ax.set_xlabel(xlabel=params.xlabel)
        ax.set_ylabel(ylabel=params.ylabel)
        ax.set_xlim(0)

    return specific_generate
