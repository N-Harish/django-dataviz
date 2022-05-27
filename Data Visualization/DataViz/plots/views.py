from django.shortcuts import render
from .visualizer import *
from .forms import *


def home(request):
    # Use a separate module to load data and visualize
    form = SelectionForm()
    df = data_loader("plots/Django_Data.xlsx")
    # plot_buc = pie_bucket(df)
    # plot_div = pie_division(df)
    plot_buc_vs_pay = box_bucket(df)
    count = 0
    if request.method == "POST":
        # Get the posted form
        MyForm = SelectionForm(request.POST)

        if MyForm.is_valid():
            formdata = MyForm.cleaned_data['select']

            if formdata == "Pie_div":
                plot_div = pie_division(df)
                count = 1
                return render(request, template_name="plots\index.html",
                              context={'form': form, "plot_div": plot_div,
                                       "plot_buc_vs_pay": plot_buc_vs_pay, "count": count})

            elif formdata == "Pie_buc":
                plot_buc = pie_bucket(df)
                count = 2
                return render(request, template_name="plots\index.html",
                              context={'form': form, 'plot_buc': plot_buc,
                                       "plot_buc_vs_pay": plot_buc_vs_pay, "count": count})
            elif formdata == "Nothing":
                return render(request, template_name="plots\index.html",
                              context={'form': form,
                                       "plot_buc_vs_pay": plot_buc_vs_pay, "count": count})

    return render(request, template_name="plots\index.html",
                  context={'form': form,
                           "plot_buc_vs_pay": plot_buc_vs_pay})
