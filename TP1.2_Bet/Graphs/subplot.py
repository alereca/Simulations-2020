def general_generate_subplot(figure):
    def specific_generate(metrics_arrays, params):
        ax = figure.add_subplot(2, 2, params.position)
        for metrics_array in metrics_arrays:
            ax.plot(
                metrics_array.data,
                metrics_array.plot_color,
                label=f"{metrics_array.color} {metrics_array.expected_value}",
            )
            if metrics_array.expected_value:
                ax.axhline(
                    metrics_array.expected_value,
                    color=metrics_array.plot_color,
                    linestyle="dashed",
                )
        ax.legend(loc="upper center", ncol=2, shadow=False, fontsize="xx-small")
        ax.set_title(label=params.title)
        ax.set_xlabel(xlabel=params.xlabel)
        ax.set_ylabel(ylabel=params.ylabel)

    return specific_generate
