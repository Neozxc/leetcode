class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(l) for l in languages]

        users_who_need_help = set()
        for u, v in friendships:
            u_idx, v_idx = u - 1, v - 1
            
            if not (lang_sets[u_idx] & lang_sets[v_idx]):
                users_who_need_help.add(u_idx)
                users_who_need_help.add(v_idx)
        
        if not users_who_need_help:
            return 0

        lang_popularity = collections.Counter()
        for user_idx in users_who_need_help:
            lang_popularity.update(lang_sets[user_idx])
    
        num_know_best_lang = 0
        if lang_popularity:
            num_know_best_lang = lang_popularity.most_common(1)[0][1]

        return len(users_who_need_help) - num_know_best_lang
