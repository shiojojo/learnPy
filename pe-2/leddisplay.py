def display(digits):

    led_display = [
        [
      "### ",
      "# # ",
      "# # ",
      "# # ",
      "### "
      ],
      [
      "  # ",
      "  # ",
      "  # ",
      "  # ",
      "  # "
      ],
      [
      "### ",
      "  # ",
      "### ",
      "#   ",
      "### "
      ],
      [
      "### ",
      "  # ",
      "### ",
      "  # ",
      "### "
      ],
      [
      "# # ",
      "# # ",
      "### ",
      "  # ",
      "  # "
      ],
      [
      "### ",
      "#   ",
      "### ",
      "  # ",
      "### "
      ],
      [
      "### ",
      "#   ",
      "### ",
      "# # ",
      "### "
      ],
      [
      "### ",
      "  # ",
      "  # ",
      "  # ",
      "  # "
      ],
      [
      "### ",
      "# # ",
      "### ",
      "# # ",
      "### "
      ],
      [
      "### ",
      "# # ",
      "### ",
      "  # ",
      "### "
      ]
    ]
    
    diplay_lst = [
        [
      "",
      "",
      "",
      "",
      ""
      ]
    ]
    for digit in digits:
        intdigit = int(digit)
        for i in range(0,5):
             diplay_lst[0][i] += led_display[intdigit][i]
    for colm in diplay_lst:
        for row in colm:
            print(row)
        

display(input("Your Number: "))