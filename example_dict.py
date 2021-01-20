def main():
    d = {
        'city': 'Portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d.get['country', 'USA'])
    d['country'] = 'AU'
    print(d.get('country', 'USA'))
    print(d)


if __name__ == '__main__':
    main()


