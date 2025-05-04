def filter_duplicate_tickets(tickets):
    seen = []                   # Список всех просмотренных тикетов
    unique_tickets = {}         # Словарь без дубликатов тикетов

    for priority in tickets:
        unique = []                      # Список уникальных тикетов для текущего приоритета
        for ticket in tickets[priority]:
            if ticket not in seen:
                unique.append(ticket)
                seen.append(ticket)
        unique_tickets[priority] = unique
    return unique_tickets


def link_severity_with_tickets(types, tickets):
    unique_tickets = filter_duplicate_tickets(tickets)
    tickets_by_type = {}
    for priority in types:
        bug_type = types[priority]
        tickets_by_type[bug_type] = unique_tickets.get(priority, [])
    return tickets_by_type


types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

print(link_severity_with_tickets(types, tickets))