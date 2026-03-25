def generate_invitations(template_content, attendees):
    """
    Generate personalized invitation files from a template
    and a list of attendees.

    Reads a template string containing placeholders ({name}, {event_title},
    {event_date}, {event_location}) and generates one output file per attendee,
    named sequentially as output_1.txt, output_2.txt, etc...
    Missing values in an attendee's data are replaced with 'N/A'.

    Args:
        template_content (str): The invitation template string containing
            placeholders to be replaced with attendee data.
        attendees (list[dict]): A list of dictionaries, each containing
            attendee information. Expected keys are 'name', 'event_title',
            'event_date', and 'event_location'.

    Returns:
        None

    Raises:
        None (errors are handled internally and logged to stdout)

    Logs:
        "Error: template must be a string"
            If template_content is not a string.
        "Error: attendees must be a list of dictionaries"
            If attendees is not a list of dictionaries.
        "Template is empty, no output files generated."
            If template_content is an empty string.
        "No data provided, no output files generated."
            If attendees is an empty list.
        "Error writing file output_X.txt"
            If an OSError occurs while writing a file.
    """

    if not isinstance(template_content, str):
        print("Error: template must be a string")
        return

    if not isinstance(
        attendees,
        list
        ) or not all(
            isinstance(x, dict) for x in attendees
            ):
        print("Error: attendees must be a list of dictionaries")
        return

    if not template_content:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):

        result = template_content
        fields = ["name", "event_title", "event_date", "event_location"]

        for field in fields:
            value = attendee.get(field)

            if value is None:
                value = "N/A"
            else:
                value = str(value)

            result = result.replace("{" + field + "}", value)

        try:
            with open(f"output_{i}.txt", "w", encoding="utf-8") as f:
                f.write(result)

        except OSError:
            print("Error writing file")
