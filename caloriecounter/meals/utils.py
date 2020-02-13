def filter_meals(params, qs):
	date_from = params.get('date_from')
	date_to = params.get('date_to')
	time_from = params.get('time_from')
	time_to = params.get('time_to')
	description = params.get('description')
	user = params.get('user')
	if date_from is not None:
		qs = qs.filter(date__gte=date_from)
	if date_to is not None:
		qs = qs.filter(date__lte=date_to)
	if time_from is not None:
		qs = qs.filter(time__gte=time_from)
	if time_to is not None:
		qs = qs.filter(time__lte=time_to)
	if description is not None:
		qs = qs.filter(description__icontains=description)
	if user is not None:
		qs = qs.filter(user_id=user)

	return qs
