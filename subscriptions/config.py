import json

from subscriptions.models import Subscription


class SubscriptionConfig:

    @classmethod
    def load_fixture_data(cls, **kwargs) -> None:
        with open('tests/fixtures/subscriptions/subscription.json', 'r') as f:
            data = json.load(f)

        # can go for bulk create but since
        # data is limited so creating one by one only
        for each_dp in data:
            subs, created = Subscription.objects.get_or_create(**each_dp)
            print(subs, created)
