{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOU0geX2zw3fbGYJYk5LkFN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DasneemDina/ds-lab/blob/main/insertion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self, dataval=None):\n",
        "    self.dataval = dataval\n",
        "    self.nextval = None\n",
        "\n",
        "class SLinkedList:\n",
        "  def __init__(self):\n",
        "    self.headval = None\n",
        "\n",
        "  def list_print(self):\n",
        "    printval = self.headval\n",
        "    while printval is not None:\n",
        "      print(printval.dataval)\n",
        "      printval = printval.nextval\n",
        "\n",
        "  def at_beginning(self, new_data):\n",
        "    new_node = Node(new_data)\n",
        "    new_node.nextval = self.headval\n",
        "    self.headval = new_node\n",
        "\n",
        "# Example usage:\n",
        "llist = SLinkedList()\n",
        "llist.headval = Node(\"Mon\")\n",
        "e2 = Node(\"Tue\")\n",
        "e3 = Node(\"Wed\")\n",
        "\n",
        "# Link first Node to second Node\n",
        "llist.headval.nextval = e2\n",
        "\n",
        "# Link second Node to third Node\n",
        "e2.nextval = e3\n",
        "\n",
        "llist.at_beginning(\"Sun\")\n",
        "\n",
        "llist.list_print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n_7HLK14E28i",
        "outputId": "aefee456-3ee8-4f67-bf9c-ba25fff811da"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sun\n",
            "Mon\n",
            "Tue\n",
            "Wed\n"
          ]
        }
      ]
    }
  ]
}