import argparse
import markdown
import json

def convert_markdown_to_html(markdown_text, theme=None):
    md = markdown.Markdown(extensions=['markdown.extensions.extra'])
    if theme:
        # This is a simplified example. In practice, you might use a library like jinja2 to apply themes.
        pass
    return md.convert(markdown_text)

def main():
    parser = argparse.ArgumentParser(description='Markdown to HTML converter with themes')
    parser.add_argument('input', type=str, help='Input Markdown file or text')
    parser.add_argument('--output', type=str, default='output.html', help='Output HTML file (default: output.html)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--theme', type=str, help='Theme to apply')

    args = parser.parse_args()

    try:
        if args.input.endswith('.md'):
            with open(args.input, 'r') as f:
                markdown_text = f.read()
        else:
            markdown_text = args.input

        html_content = convert_markdown_to_html(markdown_text, theme=args.theme)

        if args.json:
            result_dict = {'markdown': markdown_text, 'html': html_content}
            print(json.dumps(result_dict, indent=4))
        else:
            with open(args.output, 'w') as f:
                f.write(html_content)
            print(f'HTML written to {args.output}')

    except Exception as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()