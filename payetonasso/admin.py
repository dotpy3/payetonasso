from django.contrib import admin
from payetonasso import models


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	list_display = ('pk', 'name', 'message', 'price', 'fundation_name', 'fundation',
			    	'created', 'creator', 'nemopay_article_id', 'notify_creator')


@admin.register(models.IndividualTransaction)
class IndividualTransactionAdmin(admin.ModelAdmin):
	list_display = ('pk', 'transaction', 'user_name', 'user_email', 'state', 'validation')


@admin.register(models.NemopayTransaction)
class NemopayTransactionAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	list_display = ('pk', 'inv_transaction', 'created', 'nemopay_id')
